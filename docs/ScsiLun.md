# ScsiLun

The *ScsiLun* data object describes a SCSI logical unit.  A SCSI logical unit is a host device that an ESX Server or virtual machine can use for I/O operations.  An ESX Server creates SCSI logical unit objects to represent devices in the host configuration. (See the definition of *ScsiLunType_enum* for a list of the supported device types.) The vSphere API uses one of two object types to represent a SCSI logical unit, depending on the device type. - Disks containing file system volumes or parts of volumes for hosts   or raw disks for virtual machines. To represent disks, the ESX Server   creates a *HostScsiDisk* object, which inherits properties from   the *ScsiLun* base class. - Other SCSI devices, for example SCSI passthrough devices   for virtual machines. To represent one of these devices,   the ESX Server creates a *ScsiLun* object.    When the Server creates a *HostScsiDisk* or *ScsiLun* object, it specifies a valid device name and type: - *HostDevice.deviceName* - A string representing the name of the device   that is meaningful to the host. The following are some examples of   device names.     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>/dev/cdrom</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>/vmkdev/vmhba0:0:1:0</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>PhysicalDrive0</code> - *HostDevice.deviceType* - A string describing the type of device.   The following are some examples of device types.     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-cdrom</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-tape</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-disk</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-processor</code>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-unknown</code> 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier  | [optional] 
**uuid** | **str** | Universally unique identifier for the LUN used to identify ScsiLun across multiple servers.  This identifier can be used to identify analogous objects in other views such as *HostMultipathInfoLogicalUnit* and *HostScsiTopologyLun*.  See also *HostMultipathInfoLogicalUnit*, *HostScsiTopologyLun*.  | 
**descriptor** | [**List[ScsiLunDescriptor]**](ScsiLunDescriptor.md) | List of descriptors that can be used to identify the LUN object.  The uuid will also appear as a descriptor.  The id field in the descriptor is a string that can be used to correlate the ScsiLun across multiple servers. A ScsiLun may have multiple descriptors. The choice and order of these descriptors may be different on different servers.  Not all descriptors are suitable for correlation. Some descriptors are only sufficient to identify the ScsiLun within a single host. Each descriptor contains a quality property that indicates whether or not the descriptor is suitable for correlation.  ***Since:*** vSphere API 4.0  | [optional] 
**canonical_name** | **str** | Canonical name of the SCSI logical unit.  Disk partition or extent identifiers refer to this name when referring to a disk. Use this property to correlate a partition or extent to a specific SCSI disk.  See also *HostScsiDiskPartition.diskName*.  | [optional] 
**display_name** | **str** | User configurable display name of the SCSI logical unit.  A default display name will be used if available. If the display name is not supported, it will be unset. The display name does not have to be unique but it is recommended that it be unique.  ***Since:*** vSphere API 4.0  | [optional] 
**lun_type** | **str** | The type of SCSI device.  Must be one of the values of *ScsiLunType_enum*.  | 
**vendor** | **str** | The vendor of the SCSI device.  | [optional] 
**model** | **str** | The model number of the SCSI device.  | [optional] 
**revision** | **str** | The revision of the SCSI device.  | [optional] 
**scsi_level** | **int** | The SCSI level of the SCSI device.  | [optional] 
**serial_number** | **str** | The serial number of the SCSI device.  For a device that is SCSI-3 compliant, this property is derived from page 80h of the Vital Product Data (VPD), as defined by the SCSI-3 Primary Commands (SPC-3) spec. Not all SCSI-3 compliant devices provide this information. For devices that are not SCSI-3 compliant, this property is not defined.  | [optional] 
**durable_name** | [**ScsiLunDurableName**](ScsiLunDurableName.md) |  | [optional] 
**alternate_name** | [**List[ScsiLunDurableName]**](ScsiLunDurableName.md) | Alternate durable names.  Records all available durable names derived from page 80h of the Vital Product Data (VPD) and the Identification Vital Product Data (VPD) page 83h as defined by the SCSI-3 Primary Commands. For devices that are not SCSI-3 compliant this property is not defined.  ***Since:*** VI API 2.5  | [optional] 
**standard_inquiry** | **List[int]** | Standard Inquiry payload.  For a SCSI-3 compliant device this property is derived from the standard inquiry data. For devices that are not SCSI-3 compliant this property is not defined.  ***Since:*** VI API 2.5  | [optional] 
**queue_depth** | **int** | The queue depth of SCSI device.  | [optional] 
**operational_state** | **List[str]** | The operational states of the LUN.  When more than one item is present in the array, the first state should be considered the primary state. For example, a LUN may be \&quot;ok\&quot; and \&quot;degraded\&quot; indicating I/O is still possible to the LUN, but it is operating in a degraded mode.  See also *ScsiLunState_enum*.  | 
**capabilities** | [**ScsiLunCapabilities**](ScsiLunCapabilities.md) |  | [optional] 
**v_storage_support** | **str** | vStorage hardware acceleration support status.  This property represents storage acceleration provided by the SCSI logical unit. See *ScsiLunVStorageSupportStatus_enum* for valid values.  If a storage device supports hardware acceleration, the ESX host can offload specific virtual machine management operations to the storage device. With hardware assistance, the host performs storage operations faster and consumes less CPU, memory, and storage fabric bandwidth.  For vSphere 4.0 or earlier hosts, this value will be unset.  ***Since:*** vSphere API 4.1  | [optional] 
**protocol_endpoint** | **bool** | Indicates that this SCSI LUN is protocol endpoint.  This property will be populated if and only if host supports VirtualVolume based Datastore. Check the host capability *HostCapability.virtualVolumeDatastoreSupported*. See *HostProtocolEndpoint*.  ***Since:*** vSphere API 6.0  | [optional] 
**perennially_reserved** | **bool** | Indicates the state of a perennially reserved flag for a LUN.  If set for Raw Device Mapped (RDM) LUNs, the host startup or LUN rescan take comparatively shorter duration than when it is unset.  ***Since:*** vSphere API 6.7.2  | [optional] 
**clustered_vmdk_supported** | **bool** | Indicates if LUN has the prequisite properties to enable Clustered Vmdk feature once formatted into VMFS Datastore.  ***Since:*** vSphere API 7.0  | [optional] 
**application_protocol** | **str** | Indicates the current device protocol.  Application protocol for a device which is set based on input from vmkctl storage control plane. Must be one of the values of *DeviceProtocol_enum*.  | [optional] 
**dispersed_ns** | **bool** | Indicates whether namespace is dispersed.  Set to true when the namespace of LUN is dispersed.  | [optional] 

## Example

```python
from vmware_vi.models.scsi_lun import ScsiLun

# TODO update the JSON string below
json = "{}"
# create an instance of ScsiLun from a JSON string
scsi_lun_instance = ScsiLun.from_json(json)
# print the JSON string representation of the object
print ScsiLun.to_json()

# convert the object into a dict
scsi_lun_dict = scsi_lun_instance.to_dict()
# create an instance of ScsiLun from a dict
scsi_lun_form_dict = scsi_lun.from_dict(scsi_lun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


