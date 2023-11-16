# VirtualPCNet32Option

The VirtualPCNet32Option data object type defines the options for the VirtualPCNet32 data object type.  Except for the boolean supportsMorphing option, the options are inherited from the *VirtualEthernetCardOption* data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_morphing** | **bool** | Indicates that this Ethernet card supports morphing into vmxnet when appropriate.  This means that, if supportsMorphing&#x3D;\&quot;true\&quot;, the virtual AMD Lance PCNet32 Ethernet card becomes a vmxnet Ethernet card with its added performance capabilities when appropriate.  | 

## Example

```python
from vmware_vi.models.virtual_pc_net32_option import VirtualPCNet32Option

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCNet32Option from a JSON string
virtual_pc_net32_option_instance = VirtualPCNet32Option.from_json(json)
# print the JSON string representation of the object
print VirtualPCNet32Option.to_json()

# convert the object into a dict
virtual_pc_net32_option_dict = virtual_pc_net32_option_instance.to_dict()
# create an instance of VirtualPCNet32Option from a dict
virtual_pc_net32_option_form_dict = virtual_pc_net32_option.from_dict(virtual_pc_net32_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


