# OvfDuplicatedPropertyIdImport

Two or more user-configurable properties are found with the same fully-qualified property name.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_duplicated_property_id_import import OvfDuplicatedPropertyIdImport

# TODO update the JSON string below
json = "{}"
# create an instance of OvfDuplicatedPropertyIdImport from a JSON string
ovf_duplicated_property_id_import_instance = OvfDuplicatedPropertyIdImport.from_json(json)
# print the JSON string representation of the object
print OvfDuplicatedPropertyIdImport.to_json()

# convert the object into a dict
ovf_duplicated_property_id_import_dict = ovf_duplicated_property_id_import_instance.to_dict()
# create an instance of OvfDuplicatedPropertyIdImport from a dict
ovf_duplicated_property_id_import_form_dict = ovf_duplicated_property_id_import.from_dict(ovf_duplicated_property_id_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


