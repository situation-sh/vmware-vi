# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ClusterDasConfigInfoHBDatastoreCandidateEnum(str, Enum):
    """
    The policy to determine the candidates from which vCenter Server can choose heartbeat datastores.  Possible values: - `userSelectedDs`: vCenter Server chooses heartbeat datastores from the set specified   by the user (see *ClusterDasConfigInfo.heartbeatDatastore*).      More specifically,   datastores not included in the set will not be chosen. Note that if   *ClusterDasConfigInfo.heartbeatDatastore* is empty, datastore heartbeating will   be disabled for HA. - `allFeasibleDs`: vCenter Server chooses heartbeat datastores from all the feasible ones,   i.e., the datastores that are accessible to more than one host in   the cluster.      The choice will be made without giving preference to those   specified by the user (see *ClusterDasConfigInfo.heartbeatDatastore*). - `allFeasibleDsWithUserPreference`: vCenter Server chooses heartbeat datastores from all the feasible ones   while giving preference to those specified by the user (see *ClusterDasConfigInfo.heartbeatDatastore*).      More specifically, the datastores not included in *ClusterDasConfigInfo.heartbeatDatastore* will be   chosen if and only if the specified ones are not sufficient.  ***Since:*** vSphere API 5.0 
    """

    """
    allowed enum values
    """
    USERSELECTEDDS = 'userSelectedDs'
    ALLFEASIBLEDS = 'allFeasibleDs'
    ALLFEASIBLEDSWITHUSERPREFERENCE = 'allFeasibleDsWithUserPreference'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterDasConfigInfoHBDatastoreCandidateEnum from a JSON string"""
        return cls(json.loads(json_str))


