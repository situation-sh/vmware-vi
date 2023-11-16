# FcoeConfigFcoeCapabilities

Flags which indicate what parameters are settable for this FcoeConfig.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_class** | **bool** |  | 
**source_mac_address** | **bool** |  | 
**vlan_range** | **bool** |  | 

## Example

```python
from vmware_vi.models.fcoe_config_fcoe_capabilities import FcoeConfigFcoeCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of FcoeConfigFcoeCapabilities from a JSON string
fcoe_config_fcoe_capabilities_instance = FcoeConfigFcoeCapabilities.from_json(json)
# print the JSON string representation of the object
print FcoeConfigFcoeCapabilities.to_json()

# convert the object into a dict
fcoe_config_fcoe_capabilities_dict = fcoe_config_fcoe_capabilities_instance.to_dict()
# create an instance of FcoeConfigFcoeCapabilities from a dict
fcoe_config_fcoe_capabilities_form_dict = fcoe_config_fcoe_capabilities.from_dict(fcoe_config_fcoe_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


