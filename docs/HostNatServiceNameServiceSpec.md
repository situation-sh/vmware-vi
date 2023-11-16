# HostNatServiceNameServiceSpec

This data object type specifies the information for the name servers.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_auto_detect** | **bool** | The flag to indicate whether or not the DNS server should be automatically detected or specified explicitly.  ***Since:*** VI API 2.5  | 
**dns_policy** | **str** | The policy to use when multiple DNS addresses are available on the host.  ***Since:*** VI API 2.5  | 
**dns_retries** | **int** | The number of retries before giving up on a DNS request from a virtual network.  ***Since:*** VI API 2.5  | 
**dns_timeout** | **int** | The time (in seconds) before retrying a DNS request to an external network.  ***Since:*** VI API 2.5  | 
**dns_name_server** | **List[str]** | The list of DNS servers.  ***Since:*** VI API 2.5  | [optional] 
**nbds_timeout** | **int** | The time (in seconds) allotted for queries to the NetBIOS Datagram Server (NBDS).  ***Since:*** VI API 2.5  | 
**nbns_retries** | **int** | Number of retries for each query to the NBNS.  ***Since:*** VI API 2.5  | 
**nbns_timeout** | **int** | The time (in seconds) allotted for queries to the NBNS.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_nat_service_name_service_spec import HostNatServiceNameServiceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNatServiceNameServiceSpec from a JSON string
host_nat_service_name_service_spec_instance = HostNatServiceNameServiceSpec.from_json(json)
# print the JSON string representation of the object
print HostNatServiceNameServiceSpec.to_json()

# convert the object into a dict
host_nat_service_name_service_spec_dict = host_nat_service_name_service_spec_instance.to_dict()
# create an instance of HostNatServiceNameServiceSpec from a dict
host_nat_service_name_service_spec_form_dict = host_nat_service_name_service_spec.from_dict(host_nat_service_name_service_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


