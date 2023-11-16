# ArrayOfStorageDrsAutomationConfig

A boxed array of *StorageDrsAutomationConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageDrsAutomationConfig]**](StorageDrsAutomationConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_drs_automation_config import ArrayOfStorageDrsAutomationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageDrsAutomationConfig from a JSON string
array_of_storage_drs_automation_config_instance = ArrayOfStorageDrsAutomationConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageDrsAutomationConfig.to_json()

# convert the object into a dict
array_of_storage_drs_automation_config_dict = array_of_storage_drs_automation_config_instance.to_dict()
# create an instance of ArrayOfStorageDrsAutomationConfig from a dict
array_of_storage_drs_automation_config_form_dict = array_of_storage_drs_automation_config.from_dict(array_of_storage_drs_automation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


