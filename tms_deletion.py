import os
import time
import boto3
import argparse
from pprint import pprint
from helpers.utils import setup_logger


# global vars
#############
logger = args = None
#############


def setup_args():
    parser = argparse.ArgumentParser(os.path.basename(__file__))
    parser.add_argument('-d', '--description', metavar='<description_content>', type=str, default='Created by AutoMirror', help='Description content to match. Eg: "string". Default is "Created by AutoMirror".')
    parser.add_argument('-p', '--profile_name', metavar='<aws_profile_name>', type=str, default='default', help='AWS profile name to use. Eg: "custom_profile". Default is "default".')
    parser.add_argument('-v', '--verbosity', metavar='<verbosity_level>', type=str, default='INFO', help='Execution verbosity level. Eg: SUCCESS|WARN|INFO|DEBUG.')
    logger.info('Arguments parsed successfully...')
    return parser.parse_args()


def initialize_g_vars():
    global logger, args
    logger = setup_logger()
    args = setup_args()
    logger.setLevel(args.verbosity)
    logger.info('Description: {}'.format(args.description))
    logger.info('initialize_g_vars() finished successfully...')


def get_regions_list(data):
    if data and 'Regions' in data and len(data.get('Regions')) > 0:
        for region_item in data.get('Regions'):
            logger.debug('Returning: {}'.format(region_item.get('RegionName')))
            yield region_item.get('RegionName')


def find_all_sessions(client, description):
    try:
        logger.info('Starting find_all_sessions()...')
        max_results = 1000
        NextToken = res = None
        Filters=[
            {
                'Name': 'description',
                'Values': [description]
            }
        ]
        while(True):
            if NextToken is None: res = client.describe_traffic_mirror_sessions(Filters=Filters, MaxResults=1000)
            else: res = client.describe_traffic_mirror_sessions(Filters=Filters, MaxResults=1000, NextToken=NextToken)
            if res and res.get('TrafficMirrorSessions') and len(res.get('TrafficMirrorSessions')) > 0:
                session_ids = []
                for item in res.get('TrafficMirrorSessions'):
                    tms_id = item.get('TrafficMirrorSessionId')
                    tms_description = item.get('Description')
                    logger.debug('Mirror Session ID: {}\tMirror Session Description: {}'.format(tms_id, tms_description))
                    session_ids.append(tms_id)
                logger.debug('All session_ids:')
                pprint(session_ids)
                yield from session_ids
            if res and res.get('NextToken'): NextToken = res.get('NextToken')
            else: break
        logger.info('find_all_sessions() finished successfully...')
    except Exception as e:
        logger.error('Exception {} occurred in find_all_sessions()...'.format(e))
    


def delete_traffic_mirror_sessions(client, session_ids):
    try:
        session_ids = list(session_ids)
        if session_ids and len(session_ids) > 0:
            logger.info('Session IDs exist...')
            for tms_id in session_ids:
                print(tms_id)
                res = client.delete_traffic_mirror_session(TrafficMirrorSessionId=tms_id)
                if res and res.get('TrafficMirrorSessionId'):
                    logger.info('Seccussfully removed Traffic Mirror Session ID: {}...'.format(tms_id))
        logger.info('delete_traffic_mirror_sessions() finished successfully...')
    except Exception as e:
        logger.error('Exception {} occurred in delete_traffic_mirror_sessions()...'.format(e))


def main():
    try:
        initialize_g_vars()
        for region in get_regions_list(boto3.session.Session(region_name='us-east-1', profile_name=args.profile_name).client('ec2').describe_regions()):
            logger.info('Starting for region: {}'.format(region))
            client = boto3.session.Session(region_name=region, profile_name=args.profile_name).client('ec2')
            logger.info('Starting find_all_sessions() for region: {}...'.format(region))
            delete_traffic_mirror_sessions(client, find_all_sessions(client, args.description))
        logger.info('maain() finished successfully...')
    except Exception as e:
        logger.error('Exception {} occurred in main of file {}...'.format(e, os.path.basename(__file__)))


# main flow of the program
##########################
main()
##########################