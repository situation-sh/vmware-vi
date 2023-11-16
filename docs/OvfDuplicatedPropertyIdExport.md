# OvfDuplicatedPropertyIdExport

Two or more user-configurable properties are found with the same fully-qualified property name.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqid** | **str** | The fully qualified property id.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_duplicated_property_id_export import OvfDuplicatedPropertyIdExport

# TODO update the JSON string below
json = "{}"
# create an instance of OvfDuplicatedPropertyIdExport from a JSON string
ovf_duplicated_property_id_export_instance = OvfDuplicatedPropertyIdExport.from_json(json)
# print the JSON string representation of the object
print OvfDuplicatedPropertyIdExport.to_json()

# convert the object into a dict
ovf_duplicated_property_id_export_dict = ovf_duplicated_property_id_export_instance.to_dict()
# create an instance of OvfDuplicatedPropertyIdExport from a dict
ovf_duplicated_property_id_export_form_dict = ovf_duplicated_property_id_export.from_dict(ovf_duplicated_property_id_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


