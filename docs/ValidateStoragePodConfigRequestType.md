# ValidateStoragePodConfigRequestType

The parameters of *StorageResourceManager.ValidateStoragePodConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**StorageDrsConfigSpec**](StorageDrsConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.validate_storage_pod_config_request_type import ValidateStoragePodConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateStoragePodConfigRequestType from a JSON string
validate_storage_pod_config_request_type_instance = ValidateStoragePodConfigRequestType.from_json(json)
# print the JSON string representation of the object
print ValidateStoragePodConfigRequestType.to_json()

# convert the object into a dict
validate_storage_pod_config_request_type_dict = validate_storage_pod_config_request_type_instance.to_dict()
# create an instance of ValidateStoragePodConfigRequestType from a dict
validate_storage_pod_config_request_type_form_dict = validate_storage_pod_config_request_type.from_dict(validate_storage_pod_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


