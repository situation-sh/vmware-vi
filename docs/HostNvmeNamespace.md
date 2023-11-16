# HostNvmeNamespace

This data object represents an NVM Express Namespace.  In the NVME model, the underlying non-volatile storage medium is exposed via namespaces. For further information, see: - \"NVM Express over Fabrics 1.0\", Section 1.5.2,   \"NVM Subsystem\". - \"NVM Express 1.3\", section 6.1, \"Namespaces\".    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  This is a unique identifier of the NVME namespace within the host system.  ***Since:*** vSphere API 7.0  | 
**name** | **str** | The name of the namespace.  The name identifies the underlying storage exposed by the NvmeNamespace. In multipath scenarios, two namespaces can have the same name if they expose the same underlying storage through different NVME controllers.  ***Since:*** vSphere API 7.0  | 
**id** | **int** | The namespace ID is an identifier used by an NVME controller to provide access to a namespace.  The namespace ID is only unique among the namespaces attached to the same controller. For details, see: - \&quot;NVM Express 1.3\&quot;, section 6.1, \&quot;Namespaces\&quot;.    ***Since:*** vSphere API 7.0  | 
**block_size** | **int** | Block size of the namespace in bytes.  Namespaces are comprised of a number of logical blocks with a fixed size - the smallest units of data that may be read or written by the NVME controller.  ***Since:*** vSphere API 7.0  | 
**capacity_in_blocks** | **int** | The maximum number of logical blocks that may be allocated in the namespace at any point in time.  Corresponds to the NCAP field in the Identify Namespace data structure: - \&quot;NVM Express 1.3\&quot;, Section 5.15, Figure 114,   \&quot;Identify Namespace Data Structure\&quot;    ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.host_nvme_namespace import HostNvmeNamespace

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeNamespace from a JSON string
host_nvme_namespace_instance = HostNvmeNamespace.from_json(json)
# print the JSON string representation of the object
print HostNvmeNamespace.to_json()

# convert the object into a dict
host_nvme_namespace_dict = host_nvme_namespace_instance.to_dict()
# create an instance of HostNvmeNamespace from a dict
host_nvme_namespace_form_dict = host_nvme_namespace.from_dict(host_nvme_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


