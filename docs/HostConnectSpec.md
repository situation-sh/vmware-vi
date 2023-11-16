# HostConnectSpec

Specifies the parameters needed to add a single host.  This includes a small set of optional information about the host configuration. This allows the network and datastore configuration of the host to be synchronized with the naming conventions of the datacenter, as well as the configuration of a vim account (the username/password for the virtual machine files that is created on disk). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The DNS name or IP address of the host.  (Required for adding a host.)  | [optional] 
**port** | **int** | The port number for the connection.  If this is not specified, the default port number is used. For ESX 2.x hosts this is the authd port (902 by default). For ESX 3.x and above and VMware Server hosts this is the https port (443 by default). If this is a reconnect, the port number is unchanged.  | [optional] 
**ssl_thumbprint** | **str** | The thumbprint of the SSL certificate, which the host is expected to have.  If this value is set and matches the certificate thumbprint presented by the host, then the host is authenticated. If this value is not set or does not match the certificate thumbprint presented by the host, then the host&#39;s certificate is verified by checking whether it was signed by a recognized CA.  The thumbprint is always computed using the SHA1 hash and is the string representation of that hash in the format: xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx where, &#39;x&#39; represents a hexadecimal digit  ***Since:*** VI API 2.5  | [optional] 
**user_name** | **str** | The administration account on the host.  (Required for adding a host.)  | [optional] 
**password** | **str** | The password for the administration account.  (Required for adding a host.)  | [optional] 
**vm_folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**force** | **bool** | If this flag is set to \&quot;true\&quot;, then the connection succeeds even if the host is already being managed by another VirtualCenter server.  The original VirtualCenter server loses connection to the host.  | 
**vim_account_name** | **str** | The username to be used for accessing the virtual machine files on the disk.  | [optional] 
**vim_account_password** | **str** | The password to be used with the *vimAccountName* property for accessing the virtual machine files on the disk.  | [optional] 
**management_ip** | **str** | The IP address of the VirtualCenter server that will manage this host.  This field can be used to control which IP address the VirtualCenter agent will send heartbeats to. If it is not set, VirtualCenter will use the local IP address used when communicating with the host. Setting this field is useful when the VirtualCenter server is behind a NAT in which case the external NAT address must be used.  ***Since:*** vSphere API 4.0  | [optional] 
**lockdown_mode** | [**HostLockdownModeEnum**](HostLockdownModeEnum.md) |  | [optional] 
**host_gateway** | [**HostGatewaySpec**](HostGatewaySpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_connect_spec import HostConnectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostConnectSpec from a JSON string
host_connect_spec_instance = HostConnectSpec.from_json(json)
# print the JSON string representation of the object
print HostConnectSpec.to_json()

# convert the object into a dict
host_connect_spec_dict = host_connect_spec_instance.to_dict()
# create an instance of HostConnectSpec from a dict
host_connect_spec_form_dict = host_connect_spec.from_dict(host_connect_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


