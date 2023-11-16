# OvfHostResourceConstraint

Class used to indicate that the value in HostResoruce did not map to a valid reference element.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the element  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.ovf_host_resource_constraint import OvfHostResourceConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of OvfHostResourceConstraint from a JSON string
ovf_host_resource_constraint_instance = OvfHostResourceConstraint.from_json(json)
# print the JSON string representation of the object
print OvfHostResourceConstraint.to_json()

# convert the object into a dict
ovf_host_resource_constraint_dict = ovf_host_resource_constraint_instance.to_dict()
# create an instance of OvfHostResourceConstraint from a dict
ovf_host_resource_constraint_form_dict = ovf_host_resource_constraint.from_dict(ovf_host_resource_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


