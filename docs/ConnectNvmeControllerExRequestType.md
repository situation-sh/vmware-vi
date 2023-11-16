# ConnectNvmeControllerExRequestType

The parameters of *HostStorageSystem.ConnectNvmeControllerEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_spec** | [**List[HostNvmeConnectSpec]**](HostNvmeConnectSpec.md) | A list of data objects, each specifying the parameters necessary to connect to an NVMe controller.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.connect_nvme_controller_ex_request_type import ConnectNvmeControllerExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectNvmeControllerExRequestType from a JSON string
connect_nvme_controller_ex_request_type_instance = ConnectNvmeControllerExRequestType.from_json(json)
# print the JSON string representation of the object
print ConnectNvmeControllerExRequestType.to_json()

# convert the object into a dict
connect_nvme_controller_ex_request_type_dict = connect_nvme_controller_ex_request_type_instance.to_dict()
# create an instance of ConnectNvmeControllerExRequestType from a dict
connect_nvme_controller_ex_request_type_form_dict = connect_nvme_controller_ex_request_type.from_dict(connect_nvme_controller_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


