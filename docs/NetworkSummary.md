# NetworkSummary

General information about a network. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**name** | **str** | Name of the network.  | 
**accessible** | **bool** | At least one host is configured to provide this network.  | 
**ip_pool_name** | **str** | Name of the associated IP pool.  Empty if the network is not associated with an IP pool.  ***Since:*** vSphere API 4.0  | 
**ip_pool_id** | **int** | Identifier of the associated IP pool.  Zero if the network is not associated with an IP pool.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.network_summary import NetworkSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSummary from a JSON string
network_summary_instance = NetworkSummary.from_json(json)
# print the JSON string representation of the object
print NetworkSummary.to_json()

# convert the object into a dict
network_summary_dict = network_summary_instance.to_dict()
# create an instance of NetworkSummary from a dict
network_summary_form_dict = network_summary.from_dict(network_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


