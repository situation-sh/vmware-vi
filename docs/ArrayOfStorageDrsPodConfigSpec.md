# ArrayOfStorageDrsPodConfigSpec

A boxed array of *StorageDrsPodConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageDrsPodConfigSpec]**](StorageDrsPodConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_drs_pod_config_spec import ArrayOfStorageDrsPodConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageDrsPodConfigSpec from a JSON string
array_of_storage_drs_pod_config_spec_instance = ArrayOfStorageDrsPodConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageDrsPodConfigSpec.to_json()

# convert the object into a dict
array_of_storage_drs_pod_config_spec_dict = array_of_storage_drs_pod_config_spec_instance.to_dict()
# create an instance of ArrayOfStorageDrsPodConfigSpec from a dict
array_of_storage_drs_pod_config_spec_form_dict = array_of_storage_drs_pod_config_spec.from_dict(array_of_storage_drs_pod_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


