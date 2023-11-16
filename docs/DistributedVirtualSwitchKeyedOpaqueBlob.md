# DistributedVirtualSwitchKeyedOpaqueBlob

This class defines a data structure to hold opaque binary data identified by a key.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A key that identifies the opaque binary blob.  ***Since:*** vSphere API 4.0  | 
**opaque_data** | **str** | The opaque data.  It is recommended that base64 encoding be used for binary data.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_keyed_opaque_blob import DistributedVirtualSwitchKeyedOpaqueBlob

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchKeyedOpaqueBlob from a JSON string
distributed_virtual_switch_keyed_opaque_blob_instance = DistributedVirtualSwitchKeyedOpaqueBlob.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchKeyedOpaqueBlob.to_json()

# convert the object into a dict
distributed_virtual_switch_keyed_opaque_blob_dict = distributed_virtual_switch_keyed_opaque_blob_instance.to_dict()
# create an instance of DistributedVirtualSwitchKeyedOpaqueBlob from a dict
distributed_virtual_switch_keyed_opaque_blob_form_dict = distributed_virtual_switch_keyed_opaque_blob.from_dict(distributed_virtual_switch_keyed_opaque_blob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


