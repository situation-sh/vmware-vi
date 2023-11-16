# CreateDiskRequestType

The parameters of *VcenterVStorageObjectManager.CreateDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VslmCreateSpec**](VslmCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_disk_request_type import CreateDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiskRequestType from a JSON string
create_disk_request_type_instance = CreateDiskRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDiskRequestType.to_json()

# convert the object into a dict
create_disk_request_type_dict = create_disk_request_type_instance.to_dict()
# create an instance of CreateDiskRequestType from a dict
create_disk_request_type_form_dict = create_disk_request_type.from_dict(create_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


