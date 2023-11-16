# AttachDiskRequestType

The parameters of *VirtualMachine.AttachDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**controller_key** | **int** | Key of the controller the disk will connect to. It can be unset if there is only one controller (SCSI or SATA) with the available slot in the virtual machine. If there are multiple SCSI or SATA controllers available, user must specify the controller; if there is no available controllers, a *MissingController* fault will be thrown.  | [optional] 
**unit_number** | **int** | The unit number of the attached disk on its controller. If unset, the next available slot on the specified controller or the only available controller will be assigned to the attached disk.  | [optional] 

## Example

```python
from vmware_vi.models.attach_disk_request_type import AttachDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDiskRequestType from a JSON string
attach_disk_request_type_instance = AttachDiskRequestType.from_json(json)
# print the JSON string representation of the object
print AttachDiskRequestType.to_json()

# convert the object into a dict
attach_disk_request_type_dict = attach_disk_request_type_instance.to_dict()
# create an instance of AttachDiskRequestType from a dict
attach_disk_request_type_form_dict = attach_disk_request_type.from_dict(attach_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


