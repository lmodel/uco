package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A Windows PE optional header is a grouping of characteristics unique to the 'optional header' of a Windows PE (Portable Executable) file, consisting of a collection of metadata about the executable code structure of the file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsPEOptionalHeader extends UcoInherentCharacterizationThing {

  private List<Integer> addressOfEntryPoint;
  private List<Integer> baseOfCode;
  private List<Integer> checksum;
  private List<Integer> dllCharacteristics;
  private List<Integer> fileAlignment;
  private List<Integer> imageBase;
  private List<Integer> loaderFlags;
  private List<Integer> magic;
  private List<Integer> majorImageVersion;
  private List<Integer> majorLinkerVersion;
  private List<Integer> majorOSVersion;
  private List<Integer> majorSubsystemVersion;
  private List<Integer> minorImageVersion;
  private List<Integer> minorLinkerVersion;
  private List<Integer> minorOSVersion;
  private List<Integer> minorSubsystemVersion;
  private List<Integer> numberOfRVAAndSizes;
  private List<Integer> sectionAlignment;
  private List<Integer> sizeOfCode;
  private List<Integer> sizeOfHeaders;
  private List<Integer> sizeOfHeapCommit;
  private List<Integer> sizeOfHeapReserve;
  private List<Integer> sizeOfImage;
  private List<Integer> sizeOfInitializedData;
  private List<Integer> sizeOfStackCommit;
  private List<Integer> sizeOfStackReserve;
  private List<Integer> sizeOfUninitializedData;
  private List<Integer> subsystem;
  private List<Integer> win32VersionValue;


}