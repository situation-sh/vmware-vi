# HostMemoryTierFlagsEnum

Enumeration of flags pertaining to a memory tier.  Here are some examples of what the flags will look like for various memory configurations: - Traditional memory (*noTiering*): The host has a DRAM tier   for the main memory and nothing else. The DRAM tier will have the   *memoryTier* flag. - App Direct mode (*noTiering*): The host has a DRAM tier   and a PMem tier, but the two are independent and unrelated. The PMem tier is   non-volatile and is exposed as an NVDIMM device. Applications can decide whether to   direct the reads and writes to DRAM or PMem by using the appropriate system call. The   DRAM tier will have the *memoryTier* flag and the PMem tier will   have the *persistentTier* flag. - Memory mode (*hardwareTiering*): The host has a DRAM tier   and a PMem tier, but the DRAM is hidden from applications and is just a cache   for the PMem main memory. The PMem tier is volatile, and is abstracted by the hardware   layer to look like traditional memory. Applications can read from/write to memory   using the traditional memory system calls. The memory controller in the hardware will   internally direct those to the DRAM cache first, and on a cache miss redirect them to   the PMem main memory. The DRAM tier will have the *cachingTier*   flag and the PMem tier will have the *memoryTier* flag.    Possible values: - `memoryTier`: Flag indicating that the tier is the primary memory tier visible from the   host. - `persistentTier`: Flag indicating that the tier is used as non-volatile storage, e.g.      PMem in   App Direct mode. - `cachingTier`: Flag indicating that the tier is a cache for main memory.    ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


