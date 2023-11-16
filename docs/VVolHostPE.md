# VVolHostPE


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**protocol_endpoint** | [**List[HostProtocolEndpoint]**](HostProtocolEndpoint.md) | Host-specific information about the ProtocolEndpoint.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.v_vol_host_pe import VVolHostPE

# TODO update the JSON string below
json = "{}"
# create an instance of VVolHostPE from a JSON string
v_vol_host_pe_instance = VVolHostPE.from_json(json)
# print the JSON string representation of the object
print VVolHostPE.to_json()

# convert the object into a dict
v_vol_host_pe_dict = v_vol_host_pe_instance.to_dict()
# create an instance of VVolHostPE from a dict
v_vol_host_pe_form_dict = v_vol_host_pe.from_dict(v_vol_host_pe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


