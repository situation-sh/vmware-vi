# XmlToCustomizationSpecItemRequestType

The parameters of *CustomizationSpecManager.XmlToCustomizationSpecItem*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_item_xml** | **str** |  | 

## Example

```python
from vmware_vi.models.xml_to_customization_spec_item_request_type import XmlToCustomizationSpecItemRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of XmlToCustomizationSpecItemRequestType from a JSON string
xml_to_customization_spec_item_request_type_instance = XmlToCustomizationSpecItemRequestType.from_json(json)
# print the JSON string representation of the object
print XmlToCustomizationSpecItemRequestType.to_json()

# convert the object into a dict
xml_to_customization_spec_item_request_type_dict = xml_to_customization_spec_item_request_type_instance.to_dict()
# create an instance of XmlToCustomizationSpecItemRequestType from a dict
xml_to_customization_spec_item_request_type_form_dict = xml_to_customization_spec_item_request_type.from_dict(xml_to_customization_spec_item_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


