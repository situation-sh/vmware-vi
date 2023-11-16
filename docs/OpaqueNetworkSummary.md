# OpaqueNetworkSummary

The summary of a opaque network.  An object of this class is returned by the *Network.summary* property.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque_network_id** | **str** | The opaque network ID  ***Since:*** vSphere API 5.5  | 
**opaque_network_type** | **str** | The opaque network type  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.opaque_network_summary import OpaqueNetworkSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueNetworkSummary from a JSON string
opaque_network_summary_instance = OpaqueNetworkSummary.from_json(json)
# print the JSON string representation of the object
print OpaqueNetworkSummary.to_json()

# convert the object into a dict
opaque_network_summary_dict = opaque_network_summary_instance.to_dict()
# create an instance of OpaqueNetworkSummary from a dict
opaque_network_summary_form_dict = opaque_network_summary.from_dict(opaque_network_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


