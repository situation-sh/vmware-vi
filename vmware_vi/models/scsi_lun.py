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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from vmware_vi.models.host_device import HostDevice
from vmware_vi.models.scsi_lun_capabilities import ScsiLunCapabilities
from vmware_vi.models.scsi_lun_descriptor import ScsiLunDescriptor
from vmware_vi.models.scsi_lun_durable_name import ScsiLunDurableName
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScsiLun(HostDevice):
    """
    The *ScsiLun* data object describes a SCSI logical unit.  A SCSI logical unit is a host device that an ESX Server or virtual machine can use for I/O operations.  An ESX Server creates SCSI logical unit objects to represent devices in the host configuration. (See the definition of *ScsiLunType_enum* for a list of the supported device types.) The vSphere API uses one of two object types to represent a SCSI logical unit, depending on the device type. - Disks containing file system volumes or parts of volumes for hosts   or raw disks for virtual machines. To represent disks, the ESX Server   creates a *HostScsiDisk* object, which inherits properties from   the *ScsiLun* base class. - Other SCSI devices, for example SCSI passthrough devices   for virtual machines. To represent one of these devices,   the ESX Server creates a *ScsiLun* object.    When the Server creates a *HostScsiDisk* or *ScsiLun* object, it specifies a valid device name and type: - *HostDevice.deviceName* - A string representing the name of the device   that is meaningful to the host. The following are some examples of   device names.     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>/dev/cdrom</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>/vmkdev/vmhba0:0:1:0</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>PhysicalDrive0</code> - *HostDevice.deviceType* - A string describing the type of device.   The following are some examples of device types.     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-cdrom</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-tape</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-disk</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-processor</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-unknown</code> 
    """ # noqa: E501
    key: Optional[StrictStr] = Field(default=None, description="Linkable identifier ")
    uuid: StrictStr = Field(description="Universally unique identifier for the LUN used to identify ScsiLun across multiple servers.  This identifier can be used to identify analogous objects in other views such as *HostMultipathInfoLogicalUnit* and *HostScsiTopologyLun*.  See also *HostMultipathInfoLogicalUnit*, *HostScsiTopologyLun*. ")
    descriptor: Optional[List[ScsiLunDescriptor]] = Field(default=None, description="List of descriptors that can be used to identify the LUN object.  The uuid will also appear as a descriptor.  The id field in the descriptor is a string that can be used to correlate the ScsiLun across multiple servers. A ScsiLun may have multiple descriptors. The choice and order of these descriptors may be different on different servers.  Not all descriptors are suitable for correlation. Some descriptors are only sufficient to identify the ScsiLun within a single host. Each descriptor contains a quality property that indicates whether or not the descriptor is suitable for correlation.  ***Since:*** vSphere API 4.0 ")
    canonical_name: Optional[StrictStr] = Field(default=None, description="Canonical name of the SCSI logical unit.  Disk partition or extent identifiers refer to this name when referring to a disk. Use this property to correlate a partition or extent to a specific SCSI disk.  See also *HostScsiDiskPartition.diskName*. ", alias="canonicalName")
    display_name: Optional[StrictStr] = Field(default=None, description="User configurable display name of the SCSI logical unit.  A default display name will be used if available. If the display name is not supported, it will be unset. The display name does not have to be unique but it is recommended that it be unique.  ***Since:*** vSphere API 4.0 ", alias="displayName")
    lun_type: StrictStr = Field(description="The type of SCSI device.  Must be one of the values of *ScsiLunType_enum*. ", alias="lunType")
    vendor: Optional[StrictStr] = Field(default=None, description="The vendor of the SCSI device. ")
    model: Optional[StrictStr] = Field(default=None, description="The model number of the SCSI device. ")
    revision: Optional[StrictStr] = Field(default=None, description="The revision of the SCSI device. ")
    scsi_level: Optional[StrictInt] = Field(default=None, description="The SCSI level of the SCSI device. ", alias="scsiLevel")
    serial_number: Optional[StrictStr] = Field(default=None, description="The serial number of the SCSI device.  For a device that is SCSI-3 compliant, this property is derived from page 80h of the Vital Product Data (VPD), as defined by the SCSI-3 Primary Commands (SPC-3) spec. Not all SCSI-3 compliant devices provide this information. For devices that are not SCSI-3 compliant, this property is not defined. ", alias="serialNumber")
    durable_name: Optional[ScsiLunDurableName] = Field(default=None, alias="durableName")
    alternate_name: Optional[List[ScsiLunDurableName]] = Field(default=None, description="Alternate durable names.  Records all available durable names derived from page 80h of the Vital Product Data (VPD) and the Identification Vital Product Data (VPD) page 83h as defined by the SCSI-3 Primary Commands. For devices that are not SCSI-3 compliant this property is not defined.  ***Since:*** VI API 2.5 ", alias="alternateName")
    standard_inquiry: Optional[List[Annotated[int, Field(le=127, strict=True, ge=-128)]]] = Field(default=None, description="Standard Inquiry payload.  For a SCSI-3 compliant device this property is derived from the standard inquiry data. For devices that are not SCSI-3 compliant this property is not defined.  ***Since:*** VI API 2.5 ", alias="standardInquiry")
    queue_depth: Optional[StrictInt] = Field(default=None, description="The queue depth of SCSI device. ", alias="queueDepth")
    operational_state: List[StrictStr] = Field(description="The operational states of the LUN.  When more than one item is present in the array, the first state should be considered the primary state. For example, a LUN may be \"ok\" and \"degraded\" indicating I/O is still possible to the LUN, but it is operating in a degraded mode.  See also *ScsiLunState_enum*. ", alias="operationalState")
    capabilities: Optional[ScsiLunCapabilities] = None
    v_storage_support: Optional[StrictStr] = Field(default=None, description="vStorage hardware acceleration support status.  This property represents storage acceleration provided by the SCSI logical unit. See *ScsiLunVStorageSupportStatus_enum* for valid values.  If a storage device supports hardware acceleration, the ESX host can offload specific virtual machine management operations to the storage device. With hardware assistance, the host performs storage operations faster and consumes less CPU, memory, and storage fabric bandwidth.  For vSphere 4.0 or earlier hosts, this value will be unset.  ***Since:*** vSphere API 4.1 ", alias="vStorageSupport")
    protocol_endpoint: Optional[StrictBool] = Field(default=None, description="Indicates that this SCSI LUN is protocol endpoint.  This property will be populated if and only if host supports VirtualVolume based Datastore. Check the host capability *HostCapability.virtualVolumeDatastoreSupported*. See *HostProtocolEndpoint*.  ***Since:*** vSphere API 6.0 ", alias="protocolEndpoint")
    perennially_reserved: Optional[StrictBool] = Field(default=None, description="Indicates the state of a perennially reserved flag for a LUN.  If set for Raw Device Mapped (RDM) LUNs, the host startup or LUN rescan take comparatively shorter duration than when it is unset.  ***Since:*** vSphere API 6.7.2 ", alias="perenniallyReserved")
    clustered_vmdk_supported: Optional[StrictBool] = Field(default=None, description="Indicates if LUN has the prequisite properties to enable Clustered Vmdk feature once formatted into VMFS Datastore.  ***Since:*** vSphere API 7.0 ", alias="clusteredVmdkSupported")
    application_protocol: Optional[StrictStr] = Field(default=None, description="Indicates the current device protocol.  Application protocol for a device which is set based on input from vmkctl storage control plane. Must be one of the values of *DeviceProtocol_enum*. ", alias="applicationProtocol")
    dispersed_ns: Optional[StrictBool] = Field(default=None, description="Indicates whether namespace is dispersed.  Set to true when the namespace of LUN is dispersed. ", alias="dispersedNs")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','HostScsiDisk': 'HostScsiDisk'
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
    def from_json(cls, json_str: str) -> Union[Self]:
        """Create an instance of ScsiLun from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self]:
        """Create an instance of ScsiLun from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("ScsiLun failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.host_scsi_disk import HostScsiDisk
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
# TODO: Rewrite to not use raise_errors
ScsiLun.model_rebuild(raise_errors=False)
