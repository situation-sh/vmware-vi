# CustomizationCustomName

Specifies that the VirtualCenter server will launch an external application to generate the (hostname/IP).  The command line for this application must be specified in the server configuration file (vpxd.cfg) in the vpxd/name-ip-generator key. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument** | **str** | An optional argument that is passed to the utility for this IP address.  The meaning of this field is user-defined in the script.  | [optional] 

## Example

```python
from vmware_vi.models.customization_custom_name import CustomizationCustomName

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationCustomName from a JSON string
customization_custom_name_instance = CustomizationCustomName.from_json(json)
# print the JSON string representation of the object
print CustomizationCustomName.to_json()

# convert the object into a dict
customization_custom_name_dict = customization_custom_name_instance.to_dict()
# create an instance of CustomizationCustomName from a dict
customization_custom_name_form_dict = customization_custom_name.from_dict(customization_custom_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


