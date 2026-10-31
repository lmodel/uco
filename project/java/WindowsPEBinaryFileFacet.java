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
  A Windows PE binary file facet is a grouping of characteristics unique to a Windows portable executable (PE) file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsPEBinaryFileFacet extends Facet {

  private List<Integer> characteristics;
  private List<Hash> fileHeaderHashes;
  private String impHash;
  private List<String> machine;
  private Integer numberOfSections;
  private Integer numberOfSymbols;
  private WindowsPEOptionalHeader optionalHeader;
  private String peType;
  private List<String> pointerToSymbolTable;
  private List<WindowsPESection> sections;
  private Integer sizeOfOptionalHeader;
  private ZonedDateTime timeDateStamp;


}