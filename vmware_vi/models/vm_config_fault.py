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

class VmConfigFault(VimFault):
    """
    Base for configuration / environment issues that can be thrown when powering on or changing the configuration of a virtual machine.  Subclasses of this fault is also used as recent why a migration can fail. 
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
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','CannotAccessNetwork': 'CannotAccessNetwork','CannotAccessVmComponent': 'CannotAccessVmComponent','CannotAccessVmConfig': 'CannotAccessVmConfig','CannotAccessVmDevice': 'CannotAccessVmDevice','CannotAccessVmDisk': 'CannotAccessVmDisk','CannotDisableSnapshot': 'CannotDisableSnapshot','CannotUseNetwork': 'CannotUseNetwork','CpuCompatibilityUnknown': 'CpuCompatibilityUnknown','CpuHotPlugNotSupported': 'CpuHotPlugNotSupported','CpuIncompatible': 'CpuIncompatible','CpuIncompatible1ECX': 'CpuIncompatible1ECX','CpuIncompatible81EDX': 'CpuIncompatible81EDX','DVPortNotSupported': 'DVPortNotSupported','DeltaDiskFormatNotSupported': 'DeltaDiskFormatNotSupported','DestinationSwitchFull': 'DestinationSwitchFull','DeviceBackingNotSupported': 'DeviceBackingNotSupported','DeviceControllerNotSupported': 'DeviceControllerNotSupported','DeviceHotPlugNotSupported': 'DeviceHotPlugNotSupported','DeviceNotFound': 'DeviceNotFound','DeviceNotSupported': 'DeviceNotSupported','DeviceUnsupportedForVmPlatform': 'DeviceUnsupportedForVmPlatform','DeviceUnsupportedForVmVersion': 'DeviceUnsupportedForVmVersion','DigestNotSupported': 'DigestNotSupported','DisallowedDiskModeChange': 'DisallowedDiskModeChange','DiskNotSupported': 'DiskNotSupported','DrsVmotionIncompatibleFault': 'DrsVmotionIncompatibleFault','EightHostLimitViolated': 'EightHostLimitViolated','FaultToleranceCannotEditMem': 'FaultToleranceCannotEditMem','FaultToleranceCpuIncompatible': 'FaultToleranceCpuIncompatible','FeatureRequirementsNotMet': 'FeatureRequirementsNotMet','FileBackedPortNotSupported': 'FileBackedPortNotSupported','GenericVmConfigFault': 'GenericVmConfigFault','IDEDiskNotSupported': 'IDEDiskNotSupported','InvalidController': 'InvalidController','InvalidDeviceBacking': 'InvalidDeviceBacking','InvalidDeviceOperation': 'InvalidDeviceOperation','InvalidDeviceSpec': 'InvalidDeviceSpec','InvalidDiskFormat': 'InvalidDiskFormat','InvalidFormat': 'InvalidFormat','InvalidNetworkInType': 'InvalidNetworkInType','InvalidPropertyType': 'InvalidPropertyType','InvalidPropertyValue': 'InvalidPropertyValue','InvalidSnapshotFormat': 'InvalidSnapshotFormat','InvalidVmConfig': 'InvalidVmConfig','LargeRDMNotSupportedOnDatastore': 'LargeRDMNotSupportedOnDatastore','LegacyNetworkInterfaceInUse': 'LegacyNetworkInterfaceInUse','MemoryFileFormatNotSupportedByDatastore': 'MemoryFileFormatNotSupportedByDatastore','MemoryHotPlugNotSupported': 'MemoryHotPlugNotSupported','MemorySizeNotRecommended': 'MemorySizeNotRecommended','MemorySizeNotSupported': 'MemorySizeNotSupported','MemorySizeNotSupportedByDatastore': 'MemorySizeNotSupportedByDatastore','MissingController': 'MissingController','MissingIpPool': 'MissingIpPool','MissingNetworkIpConfig': 'MissingNetworkIpConfig','MultiWriterNotSupported': 'MultiWriterNotSupported','NoAvailableIp': 'NoAvailableIp','NoCompatibleHardAffinityHost': 'NoCompatibleHardAffinityHost','NoCompatibleSoftAffinityHost': 'NoCompatibleSoftAffinityHost','NoVcManagedIpConfigured': 'NoVcManagedIpConfigured','NonPersistentDisksNotSupported': 'NonPersistentDisksNotSupported','NotEnoughCpus': 'NotEnoughCpus','NotEnoughLogicalCpus': 'NotEnoughLogicalCpus','NotUserConfigurableProperty': 'NotUserConfigurableProperty','NumVirtualCoresPerSocketNotSupported': 'NumVirtualCoresPerSocketNotSupported','NumVirtualCpusIncompatible': 'NumVirtualCpusIncompatible','NumVirtualCpusNotSupported': 'NumVirtualCpusNotSupported','OvfConsumerValidationFault': 'OvfConsumerValidationFault','PhysCompatRDMNotSupported': 'PhysCompatRDMNotSupported','QuarantineModeFault': 'QuarantineModeFault','RDMNotSupported': 'RDMNotSupported','RDMNotSupportedOnDatastore': 'RDMNotSupportedOnDatastore','RDMPointsToInaccessibleDisk': 'RDMPointsToInaccessibleDisk','RawDiskNotSupported': 'RawDiskNotSupported','RemoteDeviceNotSupported': 'RemoteDeviceNotSupported','RuleViolation': 'RuleViolation','SharedBusControllerNotSupported': 'SharedBusControllerNotSupported','SoftRuleVioCorrectionDisallowed': 'SoftRuleVioCorrectionDisallowed','SoftRuleVioCorrectionImpact': 'SoftRuleVioCorrectionImpact','StorageVmotionIncompatible': 'StorageVmotionIncompatible','SwapPlacementOverrideNotSupported': 'SwapPlacementOverrideNotSupported','TooManyDevices': 'TooManyDevices','UnSupportedDatastoreForVFlash': 'UnSupportedDatastoreForVFlash','UnconfiguredPropertyValue': 'UnconfiguredPropertyValue','UnsupportedDatastore': 'UnsupportedDatastore','UnsupportedGuest': 'UnsupportedGuest','UnsupportedVmxLocation': 'UnsupportedVmxLocation','UnusedVirtualDiskBlocksNotScrubbed': 'UnusedVirtualDiskBlocksNotScrubbed','VAppNotRunning': 'VAppNotRunning','VAppPropertyFault': 'VAppPropertyFault','VFlashCacheHotConfigNotSupported': 'VFlashCacheHotConfigNotSupported','VFlashModuleNotSupported': 'VFlashModuleNotSupported','VMINotSupported': 'VMINotSupported','VMOnConflictDVPort': 'VMOnConflictDVPort','VMOnVirtualIntranet': 'VMOnVirtualIntranet','VirtualDiskBlocksNotFullyProvisioned': 'VirtualDiskBlocksNotFullyProvisioned','VirtualDiskModeNotSupported': 'VirtualDiskModeNotSupported','VirtualEthernetCardNotSupported': 'VirtualEthernetCardNotSupported','VirtualHardwareCompatibilityIssue': 'VirtualHardwareCompatibilityIssue','VirtualHardwareVersionNotSupported': 'VirtualHardwareVersionNotSupported','VmConfigIncompatibleForFaultTolerance': 'VmConfigIncompatibleForFaultTolerance','VmConfigIncompatibleForRecordReplay': 'VmConfigIncompatibleForRecordReplay','VmHostAffinityRuleViolation': 'VmHostAffinityRuleViolation','VmWwnConflict': 'VmWwnConflict','WakeOnLanNotSupported': 'WakeOnLanNotSupported'
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
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of VmConfigFault from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of VmConfigFault from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("VmConfigFault failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.cannot_access_network import CannotAccessNetwork
from vmware_vi.models.cannot_access_vm_component import CannotAccessVmComponent
from vmware_vi.models.cannot_access_vm_config import CannotAccessVmConfig
from vmware_vi.models.cannot_access_vm_device import CannotAccessVmDevice
from vmware_vi.models.cannot_access_vm_disk import CannotAccessVmDisk
from vmware_vi.models.cannot_disable_snapshot import CannotDisableSnapshot
from vmware_vi.models.cannot_use_network import CannotUseNetwork
from vmware_vi.models.cpu_compatibility_unknown import CpuCompatibilityUnknown
from vmware_vi.models.cpu_hot_plug_not_supported import CpuHotPlugNotSupported
from vmware_vi.models.cpu_incompatible import CpuIncompatible
from vmware_vi.models.cpu_incompatible1_ecx import CpuIncompatible1ECX
from vmware_vi.models.cpu_incompatible81_edx import CpuIncompatible81EDX
from vmware_vi.models.delta_disk_format_not_supported import DeltaDiskFormatNotSupported
from vmware_vi.models.destination_switch_full import DestinationSwitchFull
from vmware_vi.models.device_backing_not_supported import DeviceBackingNotSupported
from vmware_vi.models.device_controller_not_supported import DeviceControllerNotSupported
from vmware_vi.models.device_hot_plug_not_supported import DeviceHotPlugNotSupported
from vmware_vi.models.device_not_found import DeviceNotFound
from vmware_vi.models.device_not_supported import DeviceNotSupported
from vmware_vi.models.device_unsupported_for_vm_platform import DeviceUnsupportedForVmPlatform
from vmware_vi.models.device_unsupported_for_vm_version import DeviceUnsupportedForVmVersion
from vmware_vi.models.digest_not_supported import DigestNotSupported
from vmware_vi.models.disallowed_disk_mode_change import DisallowedDiskModeChange
from vmware_vi.models.disk_not_supported import DiskNotSupported
from vmware_vi.models.drs_vmotion_incompatible_fault import DrsVmotionIncompatibleFault
from vmware_vi.models.dv_port_not_supported import DVPortNotSupported
from vmware_vi.models.eight_host_limit_violated import EightHostLimitViolated
from vmware_vi.models.fault_tolerance_cannot_edit_mem import FaultToleranceCannotEditMem
from vmware_vi.models.fault_tolerance_cpu_incompatible import FaultToleranceCpuIncompatible
from vmware_vi.models.feature_requirements_not_met import FeatureRequirementsNotMet
from vmware_vi.models.file_backed_port_not_supported import FileBackedPortNotSupported
from vmware_vi.models.generic_vm_config_fault import GenericVmConfigFault
from vmware_vi.models.ide_disk_not_supported import IDEDiskNotSupported
from vmware_vi.models.invalid_controller import InvalidController
from vmware_vi.models.invalid_device_backing import InvalidDeviceBacking
from vmware_vi.models.invalid_device_operation import InvalidDeviceOperation
from vmware_vi.models.invalid_device_spec import InvalidDeviceSpec
from vmware_vi.models.invalid_disk_format import InvalidDiskFormat
from vmware_vi.models.invalid_format import InvalidFormat
from vmware_vi.models.invalid_network_in_type import InvalidNetworkInType
from vmware_vi.models.invalid_property_type import InvalidPropertyType
from vmware_vi.models.invalid_property_value import InvalidPropertyValue
from vmware_vi.models.invalid_snapshot_format import InvalidSnapshotFormat
from vmware_vi.models.invalid_vm_config import InvalidVmConfig
from vmware_vi.models.large_rdm_not_supported_on_datastore import LargeRDMNotSupportedOnDatastore
from vmware_vi.models.legacy_network_interface_in_use import LegacyNetworkInterfaceInUse
from vmware_vi.models.memory_file_format_not_supported_by_datastore import MemoryFileFormatNotSupportedByDatastore
from vmware_vi.models.memory_hot_plug_not_supported import MemoryHotPlugNotSupported
from vmware_vi.models.memory_size_not_recommended import MemorySizeNotRecommended
from vmware_vi.models.memory_size_not_supported import MemorySizeNotSupported
from vmware_vi.models.memory_size_not_supported_by_datastore import MemorySizeNotSupportedByDatastore
from vmware_vi.models.missing_controller import MissingController
from vmware_vi.models.missing_ip_pool import MissingIpPool
from vmware_vi.models.missing_network_ip_config import MissingNetworkIpConfig
from vmware_vi.models.multi_writer_not_supported import MultiWriterNotSupported
from vmware_vi.models.no_available_ip import NoAvailableIp
from vmware_vi.models.no_compatible_hard_affinity_host import NoCompatibleHardAffinityHost
from vmware_vi.models.no_compatible_soft_affinity_host import NoCompatibleSoftAffinityHost
from vmware_vi.models.no_vc_managed_ip_configured import NoVcManagedIpConfigured
from vmware_vi.models.non_persistent_disks_not_supported import NonPersistentDisksNotSupported
from vmware_vi.models.not_enough_cpus import NotEnoughCpus
from vmware_vi.models.not_enough_logical_cpus import NotEnoughLogicalCpus
from vmware_vi.models.not_user_configurable_property import NotUserConfigurableProperty
from vmware_vi.models.num_virtual_cores_per_socket_not_supported import NumVirtualCoresPerSocketNotSupported
from vmware_vi.models.num_virtual_cpus_incompatible import NumVirtualCpusIncompatible
from vmware_vi.models.num_virtual_cpus_not_supported import NumVirtualCpusNotSupported
from vmware_vi.models.ovf_consumer_validation_fault import OvfConsumerValidationFault
from vmware_vi.models.phys_compat_rdm_not_supported import PhysCompatRDMNotSupported
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
from vmware_vi.models.quarantine_mode_fault import QuarantineModeFault
from vmware_vi.models.raw_disk_not_supported import RawDiskNotSupported
from vmware_vi.models.rdm_not_supported import RDMNotSupported
from vmware_vi.models.rdm_not_supported_on_datastore import RDMNotSupportedOnDatastore
from vmware_vi.models.rdm_points_to_inaccessible_disk import RDMPointsToInaccessibleDisk
from vmware_vi.models.remote_device_not_supported import RemoteDeviceNotSupported
from vmware_vi.models.rule_violation import RuleViolation
from vmware_vi.models.shared_bus_controller_not_supported import SharedBusControllerNotSupported
from vmware_vi.models.soft_rule_vio_correction_disallowed import SoftRuleVioCorrectionDisallowed
from vmware_vi.models.soft_rule_vio_correction_impact import SoftRuleVioCorrectionImpact
from vmware_vi.models.storage_vmotion_incompatible import StorageVmotionIncompatible
from vmware_vi.models.swap_placement_override_not_supported import SwapPlacementOverrideNotSupported
from vmware_vi.models.too_many_devices import TooManyDevices
from vmware_vi.models.un_supported_datastore_for_v_flash import UnSupportedDatastoreForVFlash
from vmware_vi.models.unconfigured_property_value import UnconfiguredPropertyValue
from vmware_vi.models.unsupported_datastore import UnsupportedDatastore
from vmware_vi.models.unsupported_guest import UnsupportedGuest
from vmware_vi.models.unsupported_vmx_location import UnsupportedVmxLocation
from vmware_vi.models.unused_virtual_disk_blocks_not_scrubbed import UnusedVirtualDiskBlocksNotScrubbed
from vmware_vi.models.v_app_not_running import VAppNotRunning
from vmware_vi.models.v_app_property_fault import VAppPropertyFault
from vmware_vi.models.v_flash_cache_hot_config_not_supported import VFlashCacheHotConfigNotSupported
from vmware_vi.models.v_flash_module_not_supported import VFlashModuleNotSupported
from vmware_vi.models.virtual_disk_blocks_not_fully_provisioned import VirtualDiskBlocksNotFullyProvisioned
from vmware_vi.models.virtual_disk_mode_not_supported import VirtualDiskModeNotSupported
from vmware_vi.models.virtual_ethernet_card_not_supported import VirtualEthernetCardNotSupported
from vmware_vi.models.virtual_hardware_compatibility_issue import VirtualHardwareCompatibilityIssue
from vmware_vi.models.virtual_hardware_version_not_supported import VirtualHardwareVersionNotSupported
from vmware_vi.models.vm_config_incompatible_for_fault_tolerance import VmConfigIncompatibleForFaultTolerance
from vmware_vi.models.vm_config_incompatible_for_record_replay import VmConfigIncompatibleForRecordReplay
from vmware_vi.models.vm_host_affinity_rule_violation import VmHostAffinityRuleViolation
from vmware_vi.models.vm_wwn_conflict import VmWwnConflict
from vmware_vi.models.vmi_not_supported import VMINotSupported
from vmware_vi.models.vmon_conflict_dv_port import VMOnConflictDVPort
from vmware_vi.models.vmon_virtual_intranet import VMOnVirtualIntranet
from vmware_vi.models.wake_on_lan_not_supported import WakeOnLanNotSupported
# TODO: Rewrite to not use raise_errors
VmConfigFault.model_rebuild(raise_errors=False)
