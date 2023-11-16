# DistributedVirtualSwitchHostProductSpec

This data object type is a subset of *AboutInfo*.  An object of this type can be used to describe the specification for a host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_line_id** | **str** | The product-line name.  ***Since:*** vSphere API 4.0  | [optional] 
**version** | **str** | Dot-separated version string.  For example, \&quot;1.2\&quot;.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_host_product_spec import DistributedVirtualSwitchHostProductSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchHostProductSpec from a JSON string
distributed_virtual_switch_host_product_spec_instance = DistributedVirtualSwitchHostProductSpec.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchHostProductSpec.to_json()

# convert the object into a dict
distributed_virtual_switch_host_product_spec_dict = distributed_virtual_switch_host_product_spec_instance.to_dict()
# create an instance of DistributedVirtualSwitchHostProductSpec from a dict
distributed_virtual_switch_host_product_spec_form_dict = distributed_virtual_switch_host_product_spec.from_dict(distributed_virtual_switch_host_product_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


