# CreateStoragePodRequestType

The parameters of *Folder.CreateStoragePod*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the new storage pod.  | 

## Example

```python
from vmware_vi.models.create_storage_pod_request_type import CreateStoragePodRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStoragePodRequestType from a JSON string
create_storage_pod_request_type_instance = CreateStoragePodRequestType.from_json(json)
# print the JSON string representation of the object
print CreateStoragePodRequestType.to_json()

# convert the object into a dict
create_storage_pod_request_type_dict = create_storage_pod_request_type_instance.to_dict()
# create an instance of CreateStoragePodRequestType from a dict
create_storage_pod_request_type_form_dict = create_storage_pod_request_type.from_dict(create_storage_pod_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


