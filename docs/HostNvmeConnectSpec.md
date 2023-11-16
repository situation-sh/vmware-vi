# HostNvmeConnectSpec

Specifies the parameters necessary to connect to a regular NVME over Fabrics controller.  Here the transportParameters are used to establish a transport level connection to the specified controller. For reference, see: - \"NVM Express over Fabrics 1.0\", Section 3.3,   \"Connect command and response\"    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnqn** | **str** | NVME Qualified Name of the NVM subsystem to connect to.  Corresponds to the SUBNQN field in the Connect command as referenced above.  ***Since:*** vSphere API 7.0  | 
**controller_id** | **int** | ID of the controller to connect to within the NVM subsystem.  This field corresponds to CNTLID in the Connect command. Its usage depends on whether the NVM Subsystem supports a static or dynamic controller model. In the static model, a number of controllers may be exposed. A connection to a specific one may be requested by specifying its controller ID (which is unique only within the NVM subsystem). If a value of 0xFFFE (65534 in decimal) is provided, any one of the controllers may be allocated for the connection. In the static model a value of 0xFFFF (65535 in decimal) or above is invalid. In the dynamic model, the NVM Subsystem will dynamically allocate a controller. Any value other than 0xFFFF (65535 in decimal) specified will be consider invalid. If the controllerId is unset, it defaults to 0xFFFF (the value used in the dynamic model). Whether the NVM subsystem supports the dynamic or static model can be determined by examining the corresponding *HostNvmeDiscoveryLogEntry* returned for it.  ***Since:*** vSphere API 7.0  | [optional] 
**admin_queue_size** | **int** | Size of the admin queue which will be created once connection is established.  This field corresponds to SQSIZE in the Connect command (see above). If unset, it defaults to a reasonable value which may vary between releases (currently 16).  ***Since:*** vSphere API 7.0  | [optional] 
**keep_alive_timeout** | **int** | Timeout for the keep alive feature in seconds.  This field corresponds to KATO in the Connect command (see above). If unset, it defaults to a reasonable value which may vary between releases (currently 30 seconds). For further information, see: - \&quot;NVM Express 1.3\&quot;, Section 5.21.1.15, \&quot;Keep Alive Timer\&quot;    ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_connect_spec import HostNvmeConnectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeConnectSpec from a JSON string
host_nvme_connect_spec_instance = HostNvmeConnectSpec.from_json(json)
# print the JSON string representation of the object
print HostNvmeConnectSpec.to_json()

# convert the object into a dict
host_nvme_connect_spec_dict = host_nvme_connect_spec_instance.to_dict()
# create an instance of HostNvmeConnectSpec from a dict
host_nvme_connect_spec_form_dict = host_nvme_connect_spec.from_dict(host_nvme_connect_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


