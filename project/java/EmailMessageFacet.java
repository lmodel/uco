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
  An email message facet is a grouping of characteristics unique to a message that is an instance of an electronic mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EmailMessageFacet extends Facet {

  private ObservableObject application;
  private List<ObservableObject> bcc;
  private String body;
  private List<MimePartType> bodyMultipart;
  private ObservableObject bodyRaw;
  private List<String> categories;
  private List<ObservableObject> cc;
  private String contentDisposition;
  private String contentType;
  private ObservableObject from;
  private ObservableObject headerRaw;
  private String inReplyTo;
  private Boolean isMimeEncoded;
  private Boolean isMultipart;
  private Boolean isRead;
  private List<String> labels;
  private String messageID;
  private ZonedDateTime observableModifiedTime;
  private List<ObservableObject> observableReferences;
  private Dictionary otherHeaders;
  private String priority;
  private List<String> receivedLines;
  private ZonedDateTime receivedTime;
  private ObservableObject sender;
  private ZonedDateTime sentTime;
  private String subject;
  private List<ObservableObject> to;
  private String xMailer;
  private ObservableObject xOriginatingIP;


}