# ApplyEntitiesConfigRequestType

The parameters of *HostProfileManager.ApplyEntitiesConfig_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_config_specs** | [**List[ApplyHostProfileConfigurationSpec]**](ApplyHostProfileConfigurationSpec.md) | An array of *ApplyHostProfileConfigurationSpec* objects. Each applyConfigSpecs object contains the data objects required to remediate a host. The API caller should expand a cluster to all its hosts for the purpose of providing the required data object for configuration apply of each host.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.apply_entities_config_request_type import ApplyEntitiesConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyEntitiesConfigRequestType from a JSON string
apply_entities_config_request_type_instance = ApplyEntitiesConfigRequestType.from_json(json)
# print the JSON string representation of the object
print ApplyEntitiesConfigRequestType.to_json()

# convert the object into a dict
apply_entities_config_request_type_dict = apply_entities_config_request_type_instance.to_dict()
# create an instance of ApplyEntitiesConfigRequestType from a dict
apply_entities_config_request_type_form_dict = apply_entities_config_request_type.from_dict(apply_entities_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


