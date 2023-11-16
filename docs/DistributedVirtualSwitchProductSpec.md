# DistributedVirtualSwitchProductSpec

This data object type is a subset of *AboutInfo*.  An object of this type can be used to describe the specification for a proxy switch module of a *DistributedVirtualSwitch*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Short form of the product name.  ***Since:*** vSphere API 4.0  | [optional] 
**vendor** | **str** | Name of the vendor of this product.  ***Since:*** vSphere API 4.0  | [optional] 
**version** | **str** | Dot-separated version string.  For example, \&quot;1.2\&quot;.  ***Since:*** vSphere API 4.0  | [optional] 
**build** | **str** | Build string for the server on which this call is made.  For example, x.y.z-num. This string does not apply to the API.  ***Since:*** vSphere API 4.0  | [optional] 
**forwarding_class** | **str** | Forwarding class of the distributed virtual switch.  ***Since:*** vSphere API 4.0  | [optional] 
**bundle_id** | **str** | The ID of the bundle if a host component bundle needs to be installed on the host members to support the functionality of the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**bundle_url** | **str** | The URL of the bundle that VMware Update Manager will use to install the bundle on the host members, if *DistributedVirtualSwitchProductSpec.bundleId* is set.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_product_spec import DistributedVirtualSwitchProductSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchProductSpec from a JSON string
distributed_virtual_switch_product_spec_instance = DistributedVirtualSwitchProductSpec.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchProductSpec.to_json()

# convert the object into a dict
distributed_virtual_switch_product_spec_dict = distributed_virtual_switch_product_spec_instance.to_dict()
# create an instance of DistributedVirtualSwitchProductSpec from a dict
distributed_virtual_switch_product_spec_form_dict = distributed_virtual_switch_product_spec.from_dict(distributed_virtual_switch_product_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


