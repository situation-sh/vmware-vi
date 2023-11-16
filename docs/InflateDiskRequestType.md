# InflateDiskRequestType

The parameters of *VcenterVStorageObjectManager.InflateDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.inflate_disk_request_type import InflateDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InflateDiskRequestType from a JSON string
inflate_disk_request_type_instance = InflateDiskRequestType.from_json(json)
# print the JSON string representation of the object
print InflateDiskRequestType.to_json()

# convert the object into a dict
inflate_disk_request_type_dict = inflate_disk_request_type_instance.to_dict()
# create an instance of InflateDiskRequestType from a dict
inflate_disk_request_type_form_dict = inflate_disk_request_type.from_dict(inflate_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


