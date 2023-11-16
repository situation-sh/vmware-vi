# ExtendedElementDescription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_catalog_key_prefix** | **str** | Key to the localized message string in the catalog.  If the localized string contains parameters, values to the parameters will be provided in #messageArg. E.g: If the message in the catalog is \&quot;IP address is {address}\&quot;, value for \&quot;address\&quot; will be provided by #messageArg. Both summary and label in ElementDescription will have a corresponding entry in the message catalog with the keys &amp;lt;messageCatalogKeyPrefix&amp;gt;.summary and &amp;lt;messageCatalogKeyPrefix&amp;gt;.label respectively. ElementDescription.summary and ElementDescription.label will contain the strings in server locale.  ***Since:*** vSphere API 4.0  | 
**message_arg** | [**List[KeyAnyValue]**](KeyAnyValue.md) | Provides named arguments that can be used to localize the message in the catalog.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.extended_element_description import ExtendedElementDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedElementDescription from a JSON string
extended_element_description_instance = ExtendedElementDescription.from_json(json)
# print the JSON string representation of the object
print ExtendedElementDescription.to_json()

# convert the object into a dict
extended_element_description_dict = extended_element_description_instance.to_dict()
# create an instance of ExtendedElementDescription from a dict
extended_element_description_form_dict = extended_element_description.from_dict(extended_element_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


