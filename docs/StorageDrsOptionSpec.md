# StorageDrsOptionSpec

An incremental update to the advance settings.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | [**OptionValue**](OptionValue.md) |  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_option_spec import StorageDrsOptionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsOptionSpec from a JSON string
storage_drs_option_spec_instance = StorageDrsOptionSpec.from_json(json)
# print the JSON string representation of the object
print StorageDrsOptionSpec.to_json()

# convert the object into a dict
storage_drs_option_spec_dict = storage_drs_option_spec_instance.to_dict()
# create an instance of StorageDrsOptionSpec from a dict
storage_drs_option_spec_form_dict = storage_drs_option_spec.from_dict(storage_drs_option_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


