# OvfMissingElementNormalBoundary

If the Ovf descriptor element normal boundary is not met this exception is thrown.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundary** | **str** | The missing bound  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_missing_element_normal_boundary import OvfMissingElementNormalBoundary

# TODO update the JSON string below
json = "{}"
# create an instance of OvfMissingElementNormalBoundary from a JSON string
ovf_missing_element_normal_boundary_instance = OvfMissingElementNormalBoundary.from_json(json)
# print the JSON string representation of the object
print OvfMissingElementNormalBoundary.to_json()

# convert the object into a dict
ovf_missing_element_normal_boundary_dict = ovf_missing_element_normal_boundary_instance.to_dict()
# create an instance of OvfMissingElementNormalBoundary from a dict
ovf_missing_element_normal_boundary_form_dict = ovf_missing_element_normal_boundary.from_dict(ovf_missing_element_normal_boundary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


