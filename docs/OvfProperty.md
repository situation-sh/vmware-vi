# OvfProperty

A base fault for property faults in the property section of the Ovf XML descriptor.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the property  ***Since:*** vSphere API 4.0  | 
**value** | **str** | The value of the property  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_property import OvfProperty

# TODO update the JSON string below
json = "{}"
# create an instance of OvfProperty from a JSON string
ovf_property_instance = OvfProperty.from_json(json)
# print the JSON string representation of the object
print OvfProperty.to_json()

# convert the object into a dict
ovf_property_dict = ovf_property_instance.to_dict()
# create an instance of OvfProperty from a dict
ovf_property_form_dict = ovf_property.from_dict(ovf_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


