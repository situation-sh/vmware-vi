# VirtualDeviceFileBackingInfo

<code>*VirtualDeviceFileBackingInfo*</code> is a data object type for information about file backing for a device in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Filename for the host file used in this backing.  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**backing_object_id** | **str** | Backing object&#39;s durable and unmutable identifier.  Each backing object has a unique identifier which is not settable.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_file_backing_info import VirtualDeviceFileBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceFileBackingInfo from a JSON string
virtual_device_file_backing_info_instance = VirtualDeviceFileBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceFileBackingInfo.to_json()

# convert the object into a dict
virtual_device_file_backing_info_dict = virtual_device_file_backing_info_instance.to_dict()
# create an instance of VirtualDeviceFileBackingInfo from a dict
virtual_device_file_backing_info_form_dict = virtual_device_file_backing_info.from_dict(virtual_device_file_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


