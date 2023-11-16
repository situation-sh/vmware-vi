# OvfUnknownEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | line number where the unknown entity was found  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unknown_entity import OvfUnknownEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnknownEntity from a JSON string
ovf_unknown_entity_instance = OvfUnknownEntity.from_json(json)
# print the JSON string representation of the object
print OvfUnknownEntity.to_json()

# convert the object into a dict
ovf_unknown_entity_dict = ovf_unknown_entity_instance.to_dict()
# create an instance of OvfUnknownEntity from a dict
ovf_unknown_entity_form_dict = ovf_unknown_entity.from_dict(ovf_unknown_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


