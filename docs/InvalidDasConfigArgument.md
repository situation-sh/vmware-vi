# InvalidDasConfigArgument

This fault is thrown when an attempt is made to configure an HA cluster with invalid argument.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | **str** | The entry for the invalid argument  ***Since:*** vSphere API 5.1  | [optional] 
**cluster_name** | **str** | Name of the cluster to be configured  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.invalid_das_config_argument import InvalidDasConfigArgument

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDasConfigArgument from a JSON string
invalid_das_config_argument_instance = InvalidDasConfigArgument.from_json(json)
# print the JSON string representation of the object
print InvalidDasConfigArgument.to_json()

# convert the object into a dict
invalid_das_config_argument_dict = invalid_das_config_argument_instance.to_dict()
# create an instance of InvalidDasConfigArgument from a dict
invalid_das_config_argument_form_dict = invalid_das_config_argument.from_dict(invalid_das_config_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


