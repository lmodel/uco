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
  A PDF file facet is a grouping of characteristics unique to a PDF (Portable Document Format) file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PDFFileFacet extends Facet {

  private ControlledDictionary documentInformationDictionary;
  private Boolean isOptimized;
  private String observableVersion;
  private ZonedDateTime pdfCreationDate;
  private List<String> pdfId0;
  private String pdfId1;
  private ZonedDateTime pdfModDate;


}