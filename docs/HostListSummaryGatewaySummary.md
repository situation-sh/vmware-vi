# HostListSummaryGatewaySummary

This data object type describes information about a host gateway server that is used for the connection between vCenter Server and the host.  Gateway servers are identified by type and id. In order to use a gateway server it has to be registered with the respective type and id in the vCenter Lookup Service.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_type** | **str** | The type of the gateway server used for communication with the host.  This is an opaque string that depends on how the gateway server is registered with the vCenter Component Manager Service. There might be several gateway servers for the same type.  ***Since:*** vSphere API 6.0  | 
**gateway_id** | **str** | Unique ID of the gateway server used for communication with the host.  This ID must be a unique identifier for the gateway server as registered in the vCenter Component Manager Service. There must be only one gateway server with the same ID.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_list_summary_gateway_summary import HostListSummaryGatewaySummary

# TODO update the JSON string below
json = "{}"
# create an instance of HostListSummaryGatewaySummary from a JSON string
host_list_summary_gateway_summary_instance = HostListSummaryGatewaySummary.from_json(json)
# print the JSON string representation of the object
print HostListSummaryGatewaySummary.to_json()

# convert the object into a dict
host_list_summary_gateway_summary_dict = host_list_summary_gateway_summary_instance.to_dict()
# create an instance of HostListSummaryGatewaySummary from a dict
host_list_summary_gateway_summary_form_dict = host_list_summary_gateway_summary.from_dict(host_list_summary_gateway_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


