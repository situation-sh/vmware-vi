# AddDisksRequestType

The parameters of *HostVsanSystem.AddDisks_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**List[HostScsiDisk]**](HostScsiDisk.md) | list of disks to add for use by the VSAN service  | 

## Example

```python
from vmware_vi.models.add_disks_request_type import AddDisksRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddDisksRequestType from a JSON string
add_disks_request_type_instance = AddDisksRequestType.from_json(json)
# print the JSON string representation of the object
print AddDisksRequestType.to_json()

# convert the object into a dict
add_disks_request_type_dict = add_disks_request_type_instance.to_dict()
# create an instance of AddDisksRequestType from a dict
add_disks_request_type_form_dict = add_disks_request_type.from_dict(add_disks_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


