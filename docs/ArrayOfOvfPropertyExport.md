# ArrayOfOvfPropertyExport

A boxed array of *OvfPropertyExport*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfPropertyExport]**](OvfPropertyExport.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_property_export import ArrayOfOvfPropertyExport

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfPropertyExport from a JSON string
array_of_ovf_property_export_instance = ArrayOfOvfPropertyExport.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfPropertyExport.to_json()

# convert the object into a dict
array_of_ovf_property_export_dict = array_of_ovf_property_export_instance.to_dict()
# create an instance of ArrayOfOvfPropertyExport from a dict
array_of_ovf_property_export_form_dict = array_of_ovf_property_export.from_dict(array_of_ovf_property_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


