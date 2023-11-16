# OvfConstraint

A base fault for Ovf descriptor constraints  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the element  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.ovf_constraint import OvfConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConstraint from a JSON string
ovf_constraint_instance = OvfConstraint.from_json(json)
# print the JSON string representation of the object
print OvfConstraint.to_json()

# convert the object into a dict
ovf_constraint_dict = ovf_constraint_instance.to_dict()
# create an instance of OvfConstraint from a dict
ovf_constraint_form_dict = ovf_constraint.from_dict(ovf_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


