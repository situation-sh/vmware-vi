# HostDvxClass

Provides information about a single Device Virtualization Extensions (DVX) device class. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_class** | **str** | The class name.  | 
**checkpoint_supported** | **bool** | Indicates whether checkpointing is supported.  | 
**sw_dma_tracing_supported** | **bool** | Indicates whether software Direct Memory Access (DMA) tracing is supported.  | 
**sriov_nic** | **bool** | Indicates whether the devices of this class are SR-IOV NICs.  | 

## Example

```python
from vmware_vi.models.host_dvx_class import HostDvxClass

# TODO update the JSON string below
json = "{}"
# create an instance of HostDvxClass from a JSON string
host_dvx_class_instance = HostDvxClass.from_json(json)
# print the JSON string representation of the object
print HostDvxClass.to_json()

# convert the object into a dict
host_dvx_class_dict = host_dvx_class_instance.to_dict()
# create an instance of HostDvxClass from a dict
host_dvx_class_form_dict = host_dvx_class.from_dict(host_dvx_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


