# HostConnectInfo

This data object type contains information about a single host that can be used by the connection wizard.  This can be returned without adding the host to VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_ip** | **str** | The IP address of the VirtualCenter already managing this host, if any.  | [optional] 
**in_das_cluster** | **bool** | If the host is already being managed by a vCenter Server, this property reports true if the host is also part of a vSphere HA enabled cluster.  If this is the case, remove or disconnect the host from this cluster before adding it to another vCenter Server.  ***Since:*** vSphere API 5.0  | [optional] 
**host** | [**HostListSummary**](HostListSummary.md) |  | 
**vm** | [**List[VirtualMachineSummary]**](VirtualMachineSummary.md) | The list of virtual machines on the host.  | [optional] 
**vim_account_name_required** | **bool** | Whether or not the host requires a vimAccountName and password to be set in the ConnectSpec.  This is normally only required for VMware Server hosts.  | [optional] 
**cluster_supported** | **bool** | Whether or not the host supports clustering capabilities such as HA or DRS and therefore can be added to a cluster.  If false, the host must be added as a standalone host.  | [optional] 
**network** | [**List[HostConnectInfoNetworkInfo]**](HostConnectInfoNetworkInfo.md) | The list of network information for networks configured on this host.  | [optional] 
**datastore** | [**List[HostDatastoreConnectInfo]**](HostDatastoreConnectInfo.md) | The list of datastores on the host.  | [optional] 
**license** | [**HostLicenseConnectInfo**](HostLicenseConnectInfo.md) |  | [optional] 
**capability** | [**HostCapability**](HostCapability.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_connect_info import HostConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostConnectInfo from a JSON string
host_connect_info_instance = HostConnectInfo.from_json(json)
# print the JSON string representation of the object
print HostConnectInfo.to_json()

# convert the object into a dict
host_connect_info_dict = host_connect_info_instance.to_dict()
# create an instance of HostConnectInfo from a dict
host_connect_info_form_dict = host_connect_info.from_dict(host_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


