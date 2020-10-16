<img align="right" width="260" height="447" src="https://github.com/3CORESec/AWS-Mirror-Toolkit/raw/master/assets/imgs/mirror-officer-mascot-small.png">

# AWS Traffic Mirror Session Remover

Part of the [AWS Mirror Toolkit](https://github.com/3CORESec/aws-mirror-toolkit), AWS TMS Remover automates the removal of AWS VPC Traffic Mirror Sessions. 

[![image](https://img.shields.io/badge/BuiltOn-AWS-orange)](#)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Installation

* Clone the repository
* `pip3 install -r requirements.txt`
* AWS IAM requirements 
  * `ec2:DeleteTrafficMirrorSession`
  * `ec2:DescribeTrafficMirrorSessions`
  * `ec2:DescribeRegions`

## Usage

* Run tms_deletion.py: `python3 tms_deletion.py`
* By default `tms_deletion.py` will utilize the description that is put in place by [3CS AutoMirror](https://github.com/3CORESec/AWS-AutoMirror): `Created by AutoMirror`
  * Make the appropriate changes if you'd like to alter this behaviour. 

<img src="https://i.imgur.com/vUYgoZl.png" alt="screenshot" />

# Feedback

Found this interesting? Have a question/comment/request? Let us know! 

Feel free to open an [issue](https://github.com/3CORESec/AWS-TMS-Remover/issues) or ping us on [Twitter](https://twitter.com/3CORESec).

[![Twitter](https://img.shields.io/twitter/follow/3CORESec.svg?style=social&label=Follow)](https://twitter.com/3CORESec)
