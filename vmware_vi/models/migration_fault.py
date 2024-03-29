# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Union

from vmware_vi.models.vim_fault import VimFault
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MigrationFault(VimFault):
    """
    Base object type for issues that can occur when reassigning the execution host of a virtual machine using migrate or relocate.  These issues are typically used as argument in the MigrationEvent. When a MigrationFault is used as a value in a MigrationEvent, the type of MigrationEvent determines if the issue is a warning or an error (for example, MigrationHostWarningEvent or MigrationHostErrorEvent). When thrown as an exception, the fault is an error.  Issues are categorized as errors or warnings according to the following criteria:  If the virtual machine is powered on: 1. Error for fatal problems with the VMotion interfaces or licensing. 2. Error if VMotion would fail. 3. Error if VMotion would in any way interrupt the continuous and consistent    operation of the virtual machine. 4. Warning for potential performance or connectivity problems between the    source and destination VMotion interfaces. 5. Warning if the virtual machine's currently disconnected devices may not    be connectable after VMotion.     If the virtual machine is powered off or suspended: 1. Error if the destination host cannot access all the files that comprise    the virtual machine (including virtual disks). 2. Error if aspects of the virtual machine are not supported by the    destination host's hardware or software. 3. Warning if problems would occur when powering on or resuming the    virtual machine, if the usage/configuration of the destination    host were to remain in its current state. 
    """ # noqa: E501
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','AffinityConfigured': 'AffinityConfigured','CannotModifyConfigCpuRequirements': 'CannotModifyConfigCpuRequirements','CannotMoveVmWithDeltaDisk': 'CannotMoveVmWithDeltaDisk','CannotMoveVmWithNativeDeltaDisk': 'CannotMoveVmWithNativeDeltaDisk','CloneFromSnapshotNotSupported': 'CloneFromSnapshotNotSupported','DatacenterMismatch': 'DatacenterMismatch','DisallowedMigrationDeviceAttached': 'DisallowedMigrationDeviceAttached','DiskMoveTypeNotSupported': 'DiskMoveTypeNotSupported','FaultToleranceAntiAffinityViolated': 'FaultToleranceAntiAffinityViolated','FaultToleranceNeedsThickDisk': 'FaultToleranceNeedsThickDisk','FaultToleranceNotSameBuild': 'FaultToleranceNotSameBuild','FullStorageVMotionNotSupported': 'FullStorageVMotionNotSupported','HAErrorsAtDest': 'HAErrorsAtDest','HotSnapshotMoveNotSupported': 'HotSnapshotMoveNotSupported','IncompatibleDefaultDevice': 'IncompatibleDefaultDevice','IndependentDiskVMotionNotSupported': 'IndependentDiskVMotionNotSupported','LargeRDMConversionNotSupported': 'LargeRDMConversionNotSupported','MaintenanceModeFileMove': 'MaintenanceModeFileMove','MigrationDisabled': 'MigrationDisabled','MigrationFeatureNotSupported': 'MigrationFeatureNotSupported','MigrationNotReady': 'MigrationNotReady','MismatchedNetworkPolicies': 'MismatchedNetworkPolicies','MismatchedVMotionNetworkNames': 'MismatchedVMotionNetworkNames','NetworksMayNotBeTheSame': 'NetworksMayNotBeTheSame','NoGuestHeartbeat': 'NoGuestHeartbeat','NonHomeRDMVMotionNotSupported': 'NonHomeRDMVMotionNotSupported','RDMConversionNotSupported': 'RDMConversionNotSupported','RDMNotPreserved': 'RDMNotPreserved','ReadOnlyDisksWithLegacyDestination': 'ReadOnlyDisksWithLegacyDestination','SnapshotCloneNotSupported': 'SnapshotCloneNotSupported','SnapshotCopyNotSupported': 'SnapshotCopyNotSupported','SnapshotMoveFromNonHomeNotSupported': 'SnapshotMoveFromNonHomeNotSupported','SnapshotMoveNotSupported': 'SnapshotMoveNotSupported','SnapshotMoveToNonHomeNotSupported': 'SnapshotMoveToNonHomeNotSupported','SnapshotRevertIssue': 'SnapshotRevertIssue','StorageVMotionNotSupported': 'StorageVMotionNotSupported','SuspendedRelocateNotSupported': 'SuspendedRelocateNotSupported','TooManyDisksOnLegacyHost': 'TooManyDisksOnLegacyHost','ToolsInstallationInProgress': 'ToolsInstallationInProgress','UncommittedUndoableDisk': 'UncommittedUndoableDisk','UnsharedSwapVMotionNotSupported': 'UnsharedSwapVMotionNotSupported','VMotionAcrossNetworkNotSupported': 'VMotionAcrossNetworkNotSupported','VMotionInterfaceIssue': 'VMotionInterfaceIssue','VMotionLinkCapacityLow': 'VMotionLinkCapacityLow','VMotionLinkDown': 'VMotionLinkDown','VMotionNotConfigured': 'VMotionNotConfigured','VMotionNotLicensed': 'VMotionNotLicensed','VMotionNotSupported': 'VMotionNotSupported','VMotionProtocolIncompatible': 'VMotionProtocolIncompatible','WillLoseHAProtection': 'WillLoseHAProtection','WillModifyConfigCpuRequirements': 'WillModifyConfigCpuRequirements','WillResetSnapshotDirectory': 'WillResetSnapshotDirectory'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of MigrationFault from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of MigrationFault from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("MigrationFault failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.affinity_configured import AffinityConfigured
from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.cannot_modify_config_cpu_requirements import CannotModifyConfigCpuRequirements
from vmware_vi.models.cannot_move_vm_with_delta_disk import CannotMoveVmWithDeltaDisk
from vmware_vi.models.cannot_move_vm_with_native_delta_disk import CannotMoveVmWithNativeDeltaDisk
from vmware_vi.models.clone_from_snapshot_not_supported import CloneFromSnapshotNotSupported
from vmware_vi.models.datacenter_mismatch import DatacenterMismatch
from vmware_vi.models.disallowed_migration_device_attached import DisallowedMigrationDeviceAttached
from vmware_vi.models.disk_move_type_not_supported import DiskMoveTypeNotSupported
from vmware_vi.models.fault_tolerance_anti_affinity_violated import FaultToleranceAntiAffinityViolated
from vmware_vi.models.fault_tolerance_needs_thick_disk import FaultToleranceNeedsThickDisk
from vmware_vi.models.fault_tolerance_not_same_build import FaultToleranceNotSameBuild
from vmware_vi.models.full_storage_v_motion_not_supported import FullStorageVMotionNotSupported
from vmware_vi.models.ha_errors_at_dest import HAErrorsAtDest
from vmware_vi.models.hot_snapshot_move_not_supported import HotSnapshotMoveNotSupported
from vmware_vi.models.incompatible_default_device import IncompatibleDefaultDevice
from vmware_vi.models.independent_disk_v_motion_not_supported import IndependentDiskVMotionNotSupported
from vmware_vi.models.large_rdm_conversion_not_supported import LargeRDMConversionNotSupported
from vmware_vi.models.maintenance_mode_file_move import MaintenanceModeFileMove
from vmware_vi.models.migration_disabled import MigrationDisabled
from vmware_vi.models.migration_feature_not_supported import MigrationFeatureNotSupported
from vmware_vi.models.migration_not_ready import MigrationNotReady
from vmware_vi.models.mismatched_network_policies import MismatchedNetworkPolicies
from vmware_vi.models.mismatched_v_motion_network_names import MismatchedVMotionNetworkNames
from vmware_vi.models.networks_may_not_be_the_same import NetworksMayNotBeTheSame
from vmware_vi.models.no_guest_heartbeat import NoGuestHeartbeat
from vmware_vi.models.non_home_rdmv_motion_not_supported import NonHomeRDMVMotionNotSupported
from vmware_vi.models.primitive_binary import PrimitiveBinary
from vmware_vi.models.primitive_boolean import PrimitiveBoolean
from vmware_vi.models.primitive_byte import PrimitiveByte
from vmware_vi.models.primitive_date_time import PrimitiveDateTime
from vmware_vi.models.primitive_double import PrimitiveDouble
from vmware_vi.models.primitive_float import PrimitiveFloat
from vmware_vi.models.primitive_int import PrimitiveInt
from vmware_vi.models.primitive_long import PrimitiveLong
from vmware_vi.models.primitive_method_name import PrimitiveMethodName
from vmware_vi.models.primitive_prop_path import PrimitivePropPath
from vmware_vi.models.primitive_short import PrimitiveShort
from vmware_vi.models.primitive_string import PrimitiveString
from vmware_vi.models.primitive_type_name import PrimitiveTypeName
from vmware_vi.models.primitive_uri import PrimitiveURI
from vmware_vi.models.rdm_conversion_not_supported import RDMConversionNotSupported
from vmware_vi.models.rdm_not_preserved import RDMNotPreserved
from vmware_vi.models.read_only_disks_with_legacy_destination import ReadOnlyDisksWithLegacyDestination
from vmware_vi.models.snapshot_clone_not_supported import SnapshotCloneNotSupported
from vmware_vi.models.snapshot_copy_not_supported import SnapshotCopyNotSupported
from vmware_vi.models.snapshot_move_from_non_home_not_supported import SnapshotMoveFromNonHomeNotSupported
from vmware_vi.models.snapshot_move_not_supported import SnapshotMoveNotSupported
from vmware_vi.models.snapshot_move_to_non_home_not_supported import SnapshotMoveToNonHomeNotSupported
from vmware_vi.models.snapshot_revert_issue import SnapshotRevertIssue
from vmware_vi.models.storage_v_motion_not_supported import StorageVMotionNotSupported
from vmware_vi.models.suspended_relocate_not_supported import SuspendedRelocateNotSupported
from vmware_vi.models.too_many_disks_on_legacy_host import TooManyDisksOnLegacyHost
from vmware_vi.models.tools_installation_in_progress import ToolsInstallationInProgress
from vmware_vi.models.uncommitted_undoable_disk import UncommittedUndoableDisk
from vmware_vi.models.unshared_swap_v_motion_not_supported import UnsharedSwapVMotionNotSupported
from vmware_vi.models.v_motion_across_network_not_supported import VMotionAcrossNetworkNotSupported
from vmware_vi.models.v_motion_interface_issue import VMotionInterfaceIssue
from vmware_vi.models.v_motion_link_capacity_low import VMotionLinkCapacityLow
from vmware_vi.models.v_motion_link_down import VMotionLinkDown
from vmware_vi.models.v_motion_not_configured import VMotionNotConfigured
from vmware_vi.models.v_motion_not_licensed import VMotionNotLicensed
from vmware_vi.models.v_motion_not_supported import VMotionNotSupported
from vmware_vi.models.v_motion_protocol_incompatible import VMotionProtocolIncompatible
from vmware_vi.models.will_lose_ha_protection import WillLoseHAProtection
from vmware_vi.models.will_modify_config_cpu_requirements import WillModifyConfigCpuRequirements
from vmware_vi.models.will_reset_snapshot_directory import WillResetSnapshotDirectory
# TODO: Rewrite to not use raise_errors
MigrationFault.model_rebuild(raise_errors=False)

