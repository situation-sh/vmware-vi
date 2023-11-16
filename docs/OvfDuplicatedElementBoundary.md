# OvfDuplicatedElementBoundary

If the Ovf descriptor element have duplicated element bound.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundary** | **str** | Name of duplicated boundary  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_duplicated_element_boundary import OvfDuplicatedElementBoundary

# TODO update the JSON string below
json = "{}"
# create an instance of OvfDuplicatedElementBoundary from a JSON string
ovf_duplicated_element_boundary_instance = OvfDuplicatedElementBoundary.from_json(json)
# print the JSON string representation of the object
print OvfDuplicatedElementBoundary.to_json()

# convert the object into a dict
ovf_duplicated_element_boundary_dict = ovf_duplicated_element_boundary_instance.to_dict()
# create an instance of OvfDuplicatedElementBoundary from a dict
ovf_duplicated_element_boundary_form_dict = ovf_duplicated_element_boundary.from_dict(ovf_duplicated_element_boundary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


