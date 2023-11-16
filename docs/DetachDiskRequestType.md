# DetachDiskRequestType

The parameters of *VirtualMachine.DetachDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | [**ID**](ID.md) |  | 

## Example

```python
from vmware_vi.models.detach_disk_request_type import DetachDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DetachDiskRequestType from a JSON string
detach_disk_request_type_instance = DetachDiskRequestType.from_json(json)
# print the JSON string representation of the object
print DetachDiskRequestType.to_json()

# convert the object into a dict
detach_disk_request_type_dict = detach_disk_request_type_instance.to_dict()
# create an instance of DetachDiskRequestType from a dict
detach_disk_request_type_form_dict = detach_disk_request_type.from_dict(detach_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


