# CustomizationSpecItemToXmlRequestType

The parameters of *CustomizationSpecManager.CustomizationSpecItemToXml*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**CustomizationSpecItem**](CustomizationSpecItem.md) |  | 

## Example

```python
from vmware_vi.models.customization_spec_item_to_xml_request_type import CustomizationSpecItemToXmlRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSpecItemToXmlRequestType from a JSON string
customization_spec_item_to_xml_request_type_instance = CustomizationSpecItemToXmlRequestType.from_json(json)
# print the JSON string representation of the object
print CustomizationSpecItemToXmlRequestType.to_json()

# convert the object into a dict
customization_spec_item_to_xml_request_type_dict = customization_spec_item_to_xml_request_type_instance.to_dict()
# create an instance of CustomizationSpecItemToXmlRequestType from a dict
customization_spec_item_to_xml_request_type_form_dict = customization_spec_item_to_xml_request_type.from_dict(customization_spec_item_to_xml_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


